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

   * Analysis of CIC-IDS2017
      * Description of how it was made/collected
         * Contains most up-to-date common attacks (as of 2017)
         * Generated PCAPs
         * Uses `CICFlowMeter <https://github.com/ahlashkari/CICFlowMeter>` to generate the CSVs
         * Authors link to a `feature description page <http://ww1.netflowmeter.ca/netflowmeter.html?usid=16&utid=30620052538>`, though gives an empty page
         * Generated realistic background traffic
            * Authors used their own proposed B-Profile system (Sharafaldin, et al. 2016)
            * Built abstract behaviour of 25 users based on the HTTP, HTTPS, FTP, SSH, and email protocols.
      * Related work
      * How it relates to Ethical Hacking \(more line a general requirement of this section\)
      * Description of PCAP and relation to extracted features in the csv \(lower priority than the rest\)

   Feel free to add to this.

**Description of different recorded days**:

   The data capturing period started at 9 a.m., Monday, July 3, 2017 and ended at 5 p.m. on Friday July 7, 2017, for a total of 5 days. Monday is the normal day and only includes the benign traffic. The implemented attacks include Brute Force FTP, Brute Force SSH, DoS, Heartbleed, Web Attack, Infiltration, Botnet and DDoS. They have been executed both morning and afternoon on Tuesday, Wednesday, Thursday and Friday.


General Information 
---------------------------
CIC - Canadian Institute for Cybersecurity
IDS - Intrusion Detection System
Generated PCAP files 
Labelled Flow graphs
5 days (9 a.m. - 5 p.m.) → We use Thursday afternoon 
288602 rows × 79 columns
Labels benign (288566) and non-benign (36) → heavily unbalanced

Dataset Relevance for Ethical Hacking
---------------------------

Features
---------------------------
"Destination Port", "Flow Duration", "Total Fwd Packets", "Total Backward Packets", "Total Length of Fwd Packets", "Total Length of Bwd Packets", "Fwd Packet Length Max", "Fwd Packet Length Min", "Fwd Packet Length Mean", "Fwd Packet Length Std", "Bwd Packet Length Max", "Bwd Packet Length Min", "Bwd Packet Length Mean", "Bwd Packet Length Std", "Flow Bytes/s", "Flow Packets/s", "Flow IAT Mean", "Flow IAT Std", "Flow IAT Max", "Flow IAT Min", "Fwd IAT Total", "Fwd IAT Mean", "Fwd IAT Std", "Fwd IAT Max", "Fwd IAT Min", "Bwd IAT Total", "Bwd IAT Mean", "Bwd IAT Std", "Bwd IAT Max", "Bwd IAT Min", "Fwd PSH Flags", "Bwd PSH Flags", "Fwd URG Flags", "Bwd URG Flags", "Fwd Header Length", "Bwd Header Length", "Fwd Packets/s", "Bwd Packets/s", "Min Packet Length", "Max Packet Length", "Packet Length Mean", "Packet Length Std", "Packet Length Variance", "FIN Flag Count", "SYN Flag Count", "RST Flag Count", "PSH Flag Count", "ACK Flag Count", "URG Flag Count", "CWE Flag Count", "ECE Flag Count", "Down/Up Ratio", "Average Packet Size", "Avg Fwd Segment Size", "Avg Bwd Segment Size", "Fwd Header Length", "Fwd Avg Bytes/Bulk", "Fwd Avg Packets/Bulk", "Fwd Avg Bulk Rate", "Bwd Avg Bytes/Bulk", "Bwd Avg Packets/Bulk", "Bwd Avg Bulk Rate", "Subflow Fwd Packets", "Subflow Fwd Bytes", "Subflow Bwd Packets", "Subflow Bwd Bytes", "Init_Win_bytes_forward", "Init_Win_bytes_backward", "act_data_pkt_fwd", "min_seg_size_forward", "Active Mean", "Active Std", "Active Max", "Active Min", "Idle Mean", "Idle Std", "Idle Max", "Idle Min", "Label"


Technical information related to selected dataset subset (copied from the official dataset webpage)
---------------------------
Infiltration – Dropbox download

Meta exploit Win Vista (14:19 and 14:20-14:21 p.m.) and (14:33 -14:35)

Attacker: Kali, 205.174.165.73

Victim: Windows Vista, 192.168.10.8


Infiltration – Cool disk – MAC (14:53 p.m. – 15:00 p.m.)

Attacker: Kali, 205.174.165.73

Victim: MAC, 192.168.10.25


Infiltration – Dropbox download

Win Vista (15:04 – 15:45 p.m.)

First Step:

Attacker: Kali, 205.174.165.73

Victim: Windows Vista, 192.168.10.8


Second Step (Portscan + Nmap):

Attacker:Vista, 192.168.10.8

Victim: All other clients


Reference
---------------------------
Iman Sharafaldin, Arash Habibi Lashkari, and Ali A. Ghorbani, “Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization”, 4th International Conference on Information Systems Security and Privacy (ICISSP), Portugal, January 2018

The CICIDS2017 dataset by Sharafaldin et al. (2017) is comprised of the following vector attacks: DoS, DDoS, brute force, XSS, SQL injection, infiltration, port scan and botnet. Our selected subset contains data from Infiltration attacks. The reason why we selected this specific subset is because of its heavily unbalanced characteristics (with regard to the benign versus malicious traffic), which make it a more realistic and rerpresentative option, as in the literature and real world samples for the benign (majority) class tend to largely outweigh the minority class samples.

Table 1 :ref:`my_table_reference` demonstrates the importance of the CICIDS2017 for the Ethical Hacking research community, as it directly compares it to other existing intrusion detection datasets, clearly revealing where previous datasets are lacking and how the present dataset fits more criteria that are important for studying network attacks.

Caption: Table from Sharafaldin et al. (2017) illustration the identified Intrusion Detection datasets from previous studies compared on a taxonomy with 21 unique characteristics. CICIDS2017 contains all of them, whereas the other datasets do not appear to be as comprehensive according to the authors. The rows denote the relevant dataset and the columns refer to each specific criterion.

.. _my_table_reference:

.. table:: Comparing available IDS datasets based on the dataset evaluation framework [35].
   :widths: 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15

   +---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
   |  Network Traffic  | Interact. | Captu.  | Protocols | Attack diversity | Ano.    | Heter. | Features | Meta. | HTTP  | HTTPS | SSH  | FTP  | Email | Browser | Bforce | DoS   | Scan  | Bdoor | DNS  | Other |
   |  Label            |           |         |           |                   |         |        |          |       |      |      |      |      |       |        |        |       |       |      |      |      |
   +=========+=========+=========+=========+=========+=========+=========+=========+=========+=========+=========+=========+=========+=========+=========+=========+=========+=========+=========+=========+
   |  DARPA  | YES     | NO      | YES     | YES     | YES     | YES     | NO      | YES     | YES     | NO      | YES     | NO      | YES     | NO      | YES     | NO      | NO      | YES     | NO      | NO      | YES    |
   +---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
   |  KDD’99 | YES     | NO      | YES     | YES     | YES     | YES     | NO      | YES     | YES     | NO      | YES     | NO      | YES     | NO      | YES     | NO      | NO      | YES     | NO      | NO      | YES    |
   +---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
   |  DEFCON | NO      | NO      | NO      | YES     | YES     | YES     | NO      | YES     | NO      | NO      | NO      | NO      | YES     | YES     | NO      | YES     | -       | NO      | NO      | NO      | NO     |
   +---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
   |  CAIDAs | YES     | YES     | NO      | NO      | NO      | -       | -       | -       | -       | -       | NO      | NO      | YES     | YES     | NO      | YES     | YES     | YES     | NO      | NO      | YES    |
   +---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
   |  LBNL   | YES     | YES     | NO      | NO      | NO      | YES     | NO      | YES     | NO      | YES     | NO      | NO      | -       | -       | YES     | -       | -       | -       | YES     | NO      | NO     |
   +---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
   |  CDX    | NO      | NO      | NO      | YES     | YES     | YES     | NO      | YES     | YES     | NO      | NO      | YES     | NO      | YES     | YES     | NO      | YES     | -       | NO      | NO      | NO     |
   +---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
   |  KYOTO  | YES     | NO      | YES     | YES     | YES     | YES     | YES     | YES     | YES     | YES     | YES     | YES     | YES     | YES     | YES     | YES     | YES     | YES     | NO      | NO      | YES    |
   +---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
   |  TWENTE | YES     | YES     | YES     | YES     | YES     | YES     | NO      | YES     | NO      | YES     | NO      | YES     | NO      | YES     | NO      | NO      | YES     | NO      | YES     | -       | NO     |
   +---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
   |  UMASS  | YES     | NO      | YES     | NO      | YES     | YES     | NO      | NO      | NO      | NO      | NO      | NO      | NO      | NO      | NO      | NO      | YES     | -       | -       | NO      | NO     |
   +---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
   |  ISCX2012 | YES   | NO      | YES     | YES     | YES     | YES     | NO      | YES     | YES     | YES     | YES     | YES     | YES     | YES     | YES     | YES     | YES     | YES     | NO      | YES     | NO     |
   +---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+
   |  ADFA2013 | YES   | YES     | YES     | YES     | YES     | YES     | NO      | YES     | YES     | YES     | YES     | YES     | YES     | YES     | NO      | YES     | NO      | -       | NO      | YES     | NO     |
   +---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------+---------

 


sub header 1
-------------

This creates the toc on the right, in case we want to do it like that. however, that requires we use the same source page to add all content, which could get lengthly
