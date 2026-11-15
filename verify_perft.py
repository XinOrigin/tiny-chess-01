"""Movegen verification for src/engine.py. Run: python3 verify_perft.py"""
import importlib.util, sys, types

spec = importlib.util.spec_from_file_location("eng", "src/engine.py")
eng = importlib.util.module_from_spec(spec)
sys.modules["eng"] = eng
spec.loader.exec_module(eng)   # safe: the driver loop only runs when MAKEFUN_ENV_URL is set

INIT = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

def view(fen):
    a = fen.split()
    import re
    b = list(21*" " + "  ".join(re.sub(r"\d", lambda m: "."*int(m.group(0)), a[0]).split("/")) + 21*" ")
    b[9::10] = ["\n"]*12
    p = eng.FB("".join(b), ("Q" in a[2], "K" in a[2]), ("k" in a[2], "q" in a[2]),
               eng.parse(a[3]) if a[3] != "-" else 0, 0)
    return p if a[1] == "w" else p.rt()

def perft(pos, d):
    if d == 0: return 1
    n = 0
    for m in pos.GM():
        if pos.move(m).KC(): continue
        n += perft(pos.move(m), d-1)
    return n

CASES = [
 ("startpos d1", INIT, 1, 20), ("startpos d2", INIT, 2, 400), ("startpos d3", INIT, 3, 8902),
 ("kiwipete d1", "r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1", 1, 48),
 ("kiwipete d2", "r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1", 2, 2039),
 ("pos3 d1", "8/2p5/3p4/KP5r/1R3p1k/8/4P1P1/8 w - - 0 1", 1, 14),
 ("pos3 d2", "8/2p5/3p4/KP5r/1R3p1k/8/4P1P1/8 w - - 0 1", 2, 191),
 ("pos3 d3", "8/2p5/3p4/KP5r/1R3p1k/8/4P1P1/8 w - - 0 1", 3, 2812),
 ("promo d1", "n1n5/PPPk4/8/8/8/8/4Kppp/5N1N b - - 0 1", 1, 24),
 ("promo d2", "n1n5/PPPk4/8/8/8/8/4Kppp/5N1N b - - 0 1", 2, 496),
]
bad = 0
for name, fen, d, want in CASES:
    got = perft(view(fen), d)
    ok = got == want
    bad += 0 if ok else 1
    print(("PASS" if ok else "FAIL"), name, "got", got, "want", want)
print("ALL-PASS" if bad == 0 else "HAS-FAILURES")
