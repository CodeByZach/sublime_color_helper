# Contributing &amp; Support

## Overview

Sublime\ Versions | Description
----------------- |------------
ST3               | Fully supported and actively maintained.
ST4               | Fully supports the early development releases.

Contribution from the community is encouraged and can be done in a variety of ways:

-   Become a sponsor.
-   Bug reports.
-   Reviewing code.
-   Code patches via pull requests.
-   Documentation improvements via pull requests.

## Bug Reports

1.  Please **read the documentation** and **search the issue tracker** to try to find the answer to your question
    **before** posting an issue.

2.  When an issue is created, a [template][template] will be shown, please fill out the appropriate sections. If the
    template is not followed, the issue will be marked `Invalid` and closed.

3.  When creating an issue on the repository, please provide as much info as possible:

    -   Provide environment information by running `Preferences->Package Settings->ColorHelper->Support Info`.  The
        information will be copied to the clipboard; paste the info in issue.
    -   Errors in console.
    -   Detailed description of the problem.
    -   Examples for reproducing the error.  You can post pictures, but if specific text or code is required to
        reproduce the issue, please provide the text in a plain text format for easy copy/paste.
    -   Provide links to 3rd party syntax highlighting package you are using if applicable.

    The more info provided, the greater the chance someone will take the time to answer, implement, or fix the issue.

4.  Be prepared to answer questions and provide additional information if required.  Issues in which the creator refuses
    to respond to follow up questions will be marked as stale and closed.

## Reviewing Code

Take part in reviewing pull requests and/or reviewing direct commits.  Make suggestions to improve the code and discuss
solutions to overcome weakness in the algorithm.

## Pull Requests

Pull requests are welcome, and if you plan on contributing directly to the code, there are a couple of things to be
mindful of.

1.  Please describe the change in as much detail as possible so I can understand what is being added or modified.

2.  If you are solving a bug that does not already have an issue, please describe the bug in detail and provide info on
    how to reproduce if applicable (this is good for me and others to reference later when verifying the issue has been
    resolved).

3.  Please reference and link related open bugs or feature requests in this pull if applicable.

4.  Make sure you've documented or updated the existing documentation if introducing a new feature or modifying the
    behavior of an existing feature that a user needs to be aware of.  I will not accept new features or changes to
    existing features if you have not provided documentation describing the feature.

Continuous integration tests on are run on all pull requests and commits via Travis CI.  When making a pull request, the
tests will automatically be run, and the request must pass to be accepted.  You can (and should) run these tests before
pull requesting.  If it is not possible to run these tests locally, they will be run when the pull request is made, but
it is strongly suggested that requesters make an effort to verify before requesting to allow for a quick, smooth merge.

### Running Validation Tests

/// tip | Tip
If you are running Sublime on a Mac OS or Linux/Unix system, you run all tests by by running the shell script
(assuming you have installed your environment fulfills all requirements below):

```
chmod +x run_tests.sh
./run_tests.sh
```
///

There are a couple of dependencies that must be present before running the tests.

1.  As ST3 is the only current, actively supported version, Python 3.3 must be used to validate the tests.

2.  Unit tests are run with `pytest`.  You can install `pytest` via:

    ```
    pip install pytest
    ```

    The tests should be run from the root folder of the plugin by using the following command:

    ```
    py.test .
    ```

3.  Linting is performed on the entire project with `flake8`, `flake8-docstrings`, and `pep8-naming`.  These can be
    installed via:

    ```
    pip install flake8
    pip install flake8-docstrings
    pip install pep8-naming
    ```

    Linting is performed with the following command:

    ```
    flake8 .
    ```

## Documentation Improvements

A ton of time has been spent not only creating and supporting this plugin, but also spent making this documentation.  If
you feel it is still lacking, show your appreciation for the plugin by helping to improve the documentation.  Help with
documentation is always appreciated and can be done via pull requests.  There shouldn't be any need to run validation
tests if only updating documentation.

You don't have to render the docs locally before pull requesting, but if you wish to, I currently use a combination of
[MkDocs][mkdocs], the [Material theme][mkdocs-material], and [PyMdown Extensions][pymdown-extensions] to render the
docs.  You can preview the docs if you install these two packages.  The command for previewing the docs is
`mkdocs serve` from the root directory. You can then view the documents at `localhost:8000`.

--8<-- "refs.md"
