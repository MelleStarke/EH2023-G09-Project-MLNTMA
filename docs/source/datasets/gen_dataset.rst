General Dataset Description
===========================

This page will contain the general dataset description. in case we want to add more dataset, we can add it using this format. 

Here, ````dataset1_desc```` is the title of the page ````dataset1_desc.rst```` and also the filename. We need both to be same to get sphinx to work correctly. 

this toc creates new sub pages.


.. toctree::
   :maxdepth: 2

   dataset1_desc
   dataset2_desc


.. note::
   TODO:

   \(Not necessarily in this order:\)

   - Analysis of CIC-IDS2017
   
     - Description of how it was made/collected \(e.g. NMAP\)
     - Related work
     - How it relates to Ethical Hacking \(more line a general requirement of this section\)
     - Description of PCAP and relation to extracted features in the csv \(lower priority than the rest\)

   Feel free to add to this.
 


sub header 1
-------------

This creates the toc on the right, in case we want to do it like that. however, that requires we use the same source page to add all content, which could get lengthly