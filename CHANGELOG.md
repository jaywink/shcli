# Changelog

## [unreleased]

### Added

* Add `shcli.create` API method to create `Content`.

  Usage:
  
  ```
  import shcli
  
  shcli.create("domain.tld", "api token", "text", "visibility")
  ```
  
  Visibility parameter can be one of `public`, `limited`, `site` or `self`.
  
  Returns the created `Content` object as JSON.
