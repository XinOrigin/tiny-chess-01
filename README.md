# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/XinOrigin/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/XinOrigin/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A 4 KB Python 3.13 chess engine: alpha-beta with a transposition table, killer
moves, late-move reductions, null-move pruning and quiescence, searching a fixed
number of nodes a move (never a clock) so every trial replays byte for byte. The
node budget adapts to the opponent the environment names: 30k against the shallow
alpha-beta rungs, 55k-85k against the node-limited ones. `main.py` is
`makefun compress` output packed from `src/engine.py`.

## Run it

```sh
python3 main.py   # needs MAKEFUN_ENV_URL pointing at the env server
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
