        # Project Brief

        passhouse exists to solve a narrow, inspectable developer-tooling problem:
        Small encrypted local secrets vault with explicit safety notes.

        ## Portfolio Role

        This repository is part of the local-first engineering portfolio around
        agentic AI infrastructure, evaluation, parsing, safety boundaries, and
        small tools that can be understood from a fresh source checkout. It is not
        here to inflate repository count; it should either provide a reusable
        primitive, a benchmark surface, or a concrete local workflow.

        Topics: encryption, internet-ownership, local-first, passwords, python, release-track, secrets, self-hosted

        ## Current Gates

        - Latest completed CI: success
        - Source files counted by audit: 3
        - Test files counted by audit: 1
        - Latest release: v0.1.0
        - License: MIT

        ## Upgrade Path

        - Add a local threat model and recovery story for bad input, partial writes, and interrupted runs.
- Add a deterministic demo fixture that creates inspectable output under a temporary directory.
- Document which operations are safe by default and which require user trust.

        ## Reviewer Contract

        A serious reviewer should be able to clone the repository, read the
        README and this brief, run the tests, and understand exactly what is
        claimed. Future work should prefer deeper correctness, better fixtures,
        clearer limits, and stronger local demos over broad feature lists.
