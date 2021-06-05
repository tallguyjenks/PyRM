# Release Workflow

## Planning Releases

---

To establish a new planned release:

1. Update [ROADMAP](../ROADMAP.md)
2. Open a new [project board][0]
3. Add a new [Milestone][4]
4. Plan out work items and open [new issues][2] for them to be added to the [project board][0] and [Milestone][4]
5. Assign appropriate [issue labels][1] and using [keylabeler](../.github/keylabeler.yml) for auto tagging like `[enh]` for `Enhancement`.

---

## Active Workflow

---

1. Make a new branch off of `dev` (Gitlens and git aliases help with this)
2. Make Granular Commits
3. Keep Pull Requests small in scope (like a single feature per PR) to make approval and refactoring easier.
4. Use [Emoji-Log][5] style commit messages AND Pull Request Title's to visually indicate type of work and reduce cognitive load.
5. Open Pull Request and pass all requirements, make any requested modifications, when ready to merge, Squash merge for a cleaner working tree

---

## New Release

---

When making a new release:

1. Push to the `dev` branch
2. If all tests pass merge to `release` branch
3. When ready to initiate final release, merge `release` into `prod`
4. [Tag][3] the merge commit hash with the new version number
5. Update [ROADMAP](../ROADMAP.md) on status of tags/releases
6. Check the release drafter documentation
7. Close and update any [project boards][0]
8. Resolve any open [Milestone's][4]

---

[0]: https://github.com/tallguyjenks/PyRM/projects
[1]: https://github.com/tallguyjenks/PyRM/labels
[2]: https://github.com/tallguyjenks/PyRM/issues/new/choose
[3]: https://github.com/tallguyjenks/PyRM/tags
[4]: https://github.com/tallguyjenks/PyRM/milestones
[5]: https://github.com/ahmadawais/Emoji-Log
