aws-profile
===========

Wrapper script to generate &amp; pass AWS AssumeRole keys to other scripts

Additions

* Set the AWS_CACHE environment variable to control caching.
  Use `AWS_CACHE=false` to disable caching, or any other value
  (or unset) to keep caching enabled. When set to false the MFA
  code will be requested every time.

