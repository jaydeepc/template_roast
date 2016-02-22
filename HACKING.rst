CloudCafe Style Guide
=====================


General Guidelines
------------------
1. It is **HIGHLY** encouraged that if you have not already read (and even if
   it's been a while since you have) the Python Enhancement Proposals (PEPs)
   PEP-8 and PEP 20 that you do so.
2. Guidelines here are intended to help encourage code unity, they are not
   unbreakable rules, but should be adhered to failing a good reason not to.
3. When in doubt, **ALL** code should conform either directly to or in the
   spirit of Python PEP 20, if you are still in doubt, go with Python PEP-8.
4. If you really are still in doubt, see Guideline 2.
5. Base Classes are your friend. Use them when they make sense.


Development Guidelines
----------------------
- Always use **SPACES**. **NEVER TABS**. All block indention should be
  four (4) spaces.
- Avoid single letter variable names except in the case of iterators,
  in which case a descriptive variable name would still be preferable
  if possible.
- Do not leave trailing whitespace or whitespace in blank lines.
- Put two newlines between top-level code (funcs, classes, etc).
- Use only UNIX style newlines ("\n"), not Windows style ("\r\n").
- Put one newline between methods in classes and anywhere else.
- Long lines should be wrapped in parentheses in preference to using
  a backslash for line continuation.
- Do not write "except:", use "except Exception:" at the very least
- Use try/except where logical. Avoid wrapping large blocks of code in
  in huge try/except blocks.
- Use Enumerated Types where logical to pass around string constants
  or magic numbers between Functions, Methods, Classes and Packages.
  Python does not provide a default Enumerated Type data type, CloudCafe uses
  Class structs by naming convention in their place.

Example::
  class ComputeServerStates(object):
      ACTIVE = "ACTIVE"
      BUILD = "BUILD"
      REBUILD = "REBUILD"
      ERROR = "ERROR"
      DELETING = "DELETING"
      DELETED = "DELETED"
      RESCUE = "RESCUE"
      PREP_RESCUE = "PREP_RESCUE"
      RESIZE = "RESIZE"
      VERIFY_RESIZE = "VERIFY_RESIZE"

- Blocks of code should either be self documenting and/or well commented,
  especially in cases of non-standard code.
- Use Python list comprehensions when possible. They can make large blocks
  of code collapse to a single line.
- String formatting via the new (as of python 2.4) .format() method is
  preferred over the older %s style encoding and ''.join() methods.
  (Note on ''.join():  This is OK to use and encouraged *if* you're actually
  creating a string from a large list of strings. Otherwise, ''.format()
  is the better choice).


Test Data/Configuration
-----------------------
- Tests should make no assumptions on data exists. Test data should either
  be generated in a fixture, or be provided in a configuration file.
- Tests should be self contained. They should not rely on changes in state
  not performed in the test. The one exception to this rule is ordered tests,
  but even those are discouraged unless absolutely necessary.
- Each test/test class is responsible for deleting/or removing any resources
  creating during the test.


Imports
-------
- Do not use wildcard ``*`` import
- Do not make relative imports
- Order your imports by the full module path


Docstrings
----------
Example::

  """A one line docstring looks like this and ends in a period."""


  """A multi line docstring has a one-line summary, less than 80 characters.

  Then a new paragraph after a newline that explains in more detail any
  general information about the function, class or method. Example usages
  are also great to have here if it is a complex class for function.

  When writing the docstring for a class, an extra line should be placed
  after the closing quotations. For more in-depth explanations for these
  decisions see http://www.python.org/dev/peps/pep-0257/
  """


Before Committing
-----------------
- Follow the general OpenStack submission workflow
  (http://docs.openstack.org/infra/manual/developers.html#development-workflow). This means all
  all submissions should be squashed into one commit with one commit id
  and be submitted from a feature branch, not master.
- Always run a PEP8 check on your modified code before committing.
  You can do this with a plethora of tools such as flake8, pylint,
  and pyflakes.  **Once gating on PEP-8 rules is enabled, Gerrit will
  immediately reject any submission with PEP-8 issues.**
- Blocks of commented out code should not be submitted to trunk except
  in extraordinary cases.
- Tests that either validate nothing or simply have the "pass" statement
  should not be submitted.
- Only functional, **TESTED CODE** should be committed. There are no
  exceptions. This includes verify that code for other projects has not been
  broken if your changes effect common code. Until a gate job is in place,
  it is not time efficient for reviewers to execute all submitted code.


Commit Messages
---------------
Using a common format for commit messages will help keep our git history
readable. Follow these guidelines:

  First, provide a brief summary of 50 characters or less.

  The first line of the commit message should provide an accurate
  description of the change, not just a reference to a bug or
  blueprint. It must be followed by a single blank line.

  Following your brief summary, provide a more detailed description of
  the patch, manually wrapping the text at 72 characters. This
  description should provide enough detail that one does not have to
  refer to external resources to determine its high-level functionality.

  Once you use 'git review', two lines will be appended to the commit
  message: a blank line followed by a 'Change-Id'. This is important
  to correlate this commit with a specific review in Gerrit, and it
  should not be modified.

For further information on constructing high quality commit messages,
and how to split up commits into a series of changes, consult the
project wiki:

   http://wiki.openstack.org/GitCommitMessages