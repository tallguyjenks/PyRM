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

1. Assign the issue to yourself to begin work on it
2. Create a `feature` branch off of the `dev` branch. `git switch -c feature dev`
3. Make sure to have atomic commits and contextual commit messages using [Emoji-Log][5] for both the commit messages, and pull request titles.
4. Keep Pull Requests small in scope (like a single feature per PR) to make approval and refactoring easier.
5. Push your local `feature` branch to your remote repository on github `git push -u origin feature`
6. Open a [new merge/pull request][6] and in your pull request reference the issue the pull request is for by it's number, ex: `resolves #11`
7. Pull Request must pass Linting, Unit Tests, and any other checks for a passing build to be considered ready for manual review and feedback.

---

## New Release

---

When making a new release:

1. Push to the `dev` branch
2. If all tests pass merge to `prod` branch
3. When ready to initiate final release, merge `prod` into `release`
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
[6]: https://github.com/tallguyjenks/PyRM/compare
