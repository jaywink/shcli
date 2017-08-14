# Changelog

## [0.1.4] - 2017-08-14

No functional changes, release to fix packaging issues.

## [0.1.3] - 2017-08-14

### Added

* Add `shcli.create` API method to create `Content`.

  Usage:
  
  ```
  import shcli
  
  shcli.create("domain.tld", "api token", "text", "visibility")
  ```
  
  Visibility parameter can be one of `public`, `limited`, `site` or `self`.
  
  Returns the created `Content` object as JSON.

* Add command line script to use `create` command.

  Type `shcli create --help` for usage.
