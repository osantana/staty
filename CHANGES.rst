1.1.1
-----

  - Replace bumpversion support with CHANGES.rst option
  - Add support for setup.py version command
  - Adopt twine for PyPI release/upload
  - Use README.rst as a long description at PyPI
  - Update some requirements

1.1.0
-----

  - Add an HTTPStatus base class for type annotation usage

1.0.0
-----

  - Refactor status check/test implementation
  - Add numeric code to status map

0.5.0
-----

  - Remove HTTP statuses global maps
  - Create global StatusMap registry with constant attributes support
  - Add support for HTTP code comparison with integers, strings, HTTP classes, etc
  - Improve documentation organization, presentation and formatting

0.4.3
-----

  - Fixed CI and documentation builds

0.4.2
-----

  - Fix setup.py errors

0.4.0
-----

  - Add initial documentation
  - Update dev requirements
  - Configure bumpversion for library release

0.3.1
-----

  - Fix SwitchProxy class message

0.3.0
-----

  - Add RFC references when available.

0.2.2
-----

  - Small refactoring in HTTPError class implementation

0.2.1
-----

  - Fix CI (travis/tox) errors

0.2
---

  - Initial support for requests response handling and wrapping.
  - Exception mixins must be derived from mixins to be used with try:/except:
  - Minor improvements and :lipstick: in code formatting and project organization

0.1
---

  - First version
