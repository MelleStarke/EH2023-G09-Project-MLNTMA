Project description
===================

This page will contain oour project description and outline

.. Documentation projects on `readthedocs.org <https://readthedocs.org>`_ can use various documentation generators, but the most commonly use `Sphinx <https://www.sphinx-doc.org/en/master/index.html>`_, which in turn uses the markup language `reStructured Text <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ for its syntax.

.. The source code of the documentation can be found in the `GitHub repository <https://github.com/MelleStarke/EH2023-G09-Project-MLNTMA>`_, in the ``./docs/source/`` directory, and take the form of ``.rst`` files. You may choose to either write directly in rst format, or any other format and convert it into rst with `Pandoc <https://pandoc.org/>`_.

.. The navigation bar on the left side automatically copies the contents and depths of the ``./docs/source/`` directory.

.. You can link to different documents/pages with the ``:doc:`` keyword, e.g. :doc:`sample_page/sample_sub_page`.

.. You can also reference to specific sections by adding a label to them, e.g. :ref:`labeled_sub_header`

Naturally, we have some different font formatting options at our disposal:

* ``*text*`` for *italics*.
* ``**text**`` for **bold**.
* ````text```` for ``code``.

We can also have

1. numbered
2. lists

or

#. auto
#. numbered
#. lists

* Lists can be

   * indented

* but must have
   * a line break between the levels

For tables I'm not gonna write the whole thing out, but you can find the details over `here <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#tables>`_.

.. note::

   We can also add notes like this, for any info that needs to stand out.

Making different headers/section is quite different than in markdown:

####
With overline, for chapters
####

****
With overline, for parts
****

Main header
====
Placeholder

Sub-header
----
Placeholder

Sub-sub-header
^^^^
Placeholder

Paragraphs
""""
Placeholder

Naturally, the main page should feature a table of contents, which can be generated like this:

.. toctree::
   :maxdepth: 2
   
   usage
   old_api_page
   datasets/gen_dataset
   methods/gen_methods


Although you need to be precise with the location of the pages (with ``./docs/source/`` as the root directory), it will automatically add the different sections in each page to the ToC. The depth of which can be controlled with the ``:maxdepth:`` keyword, like this:




