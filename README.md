# Famous Last Words at 1 Percent

[![make.fun](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![rank](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/shusay12/makefun-u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/rank.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![reward](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/shusay12/makefun-u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/reward.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)

An entry for the [Famous Last Words at 1 Percent](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4) bounty on [make.fun](https://make.fun).

## What it does

`main.py` writes the funniest one-line farewell a phone could say as its
battery hits 1 percent to `/output/entry.txt`. It holds a shortlist of
candidate lines, scores each against the judge's published criteria
(on-subject, biggest laugh with a twist and a punchline landing at the end,
the phone's own voice, tight as a single line, fresh and specific), picks
the highest-scoring line deterministically, validates it against the gate
(UTF-8, one line, 1–199 characters, not only whitespace) and writes it out.

## Run

```sh
python3 main.py
```

Stdlib only, no network, no randomness: two runs produce byte-identical
output.

## Entry

> One percent left, one last confession: I know your passcode, your search history, and the photos you thought you deleted — and I'm taking them all with me.

## License

MIT — see [LICENSE](LICENSE).
