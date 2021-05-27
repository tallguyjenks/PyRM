# Release Workflow

## Planning Releases

---

To establish a new planned release:

1. Update [ROADMAP](../ROADMAP.md)
2. Open a new [project board][0]
3. Make new [issue labels][1] on github for the release tag
4. Update [keylabeler](../.github/keylabeler.yml) for new version auto tagging like `"[010]": v0.1.0`
5. Add a new [Milestone][4]
6. Plan out work items and open [new issues][2] for them to be added to the [project board][0]

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
