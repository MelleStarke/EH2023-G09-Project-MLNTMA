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


**Authors previously outlined 11 critera for building a reliable benchmark dataset:**

   In our recent dataset evaluation framework (Gharib et al., 2016), we have identified eleven criteria that are necessary for building a reliable benchmark dataset. None of the previous IDS datasets could cover all of the 11 criteria. In the following, we briefly outline these criteria:

   Complete Network configuration: A complete network topology includes Modem, Firewall, Switches, Routers, and presence of a variety of operating systems such as Windows, Ubuntu and Mac OS X.

   Complete Traffic: By having a user profiling agent and 12 different machines in Victim-Network and real attacks from the Attack-Network.

   Labelled Dataset: Section 4 and Table 2 show the benign and attack labels for each day. Also, the details of the attack timing will be published on the dataset document.

   Complete Interaction: As Figure 1 shows, we covered both within and between internal LAN by having two different networks and Internet communication as well.

   Complete Capture: Because we used the mirror port, such as tapping system, all traffics have been captured and recorded on the storage server.

   Available Protocols: Provided the presence of all common available protocols, such as HTTP, HTTPS, FTP, SSH and email protocols.

   Attack Diversity: Included the most common attacks based on the 2016 McAfee report, such as Web based, Brute force, DoS, DDoS, Infiltration, Heart-bleed, Bot and Scan covered in this dataset.

   Heterogeneity: Captured the network traffic from the main Switch and memory dump and system calls from all victim machines, during the attacks execution.

   Feature Set: Extracted more than 80 network flow features from the generated network traffic using CICFlowMeter and delivered the network flow dataset as a CSV file. See our PCAP analyzer and CSV generator.

   MetaData: Completely explained the dataset which includes the time, attacks, flows and labels in the published paper.

   The full research paper outlining the details of the dataset and its underlying principles:

    Iman Sharafaldin, Arash Habibi Lashkari, and Ali A. Ghorbani, “Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization”, 4th International Conference on Information Systems Security and Privacy (ICISSP), Purtogal, January 2018


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
-------------------------------------

Features
---------------------------
"Destination Port", "Flow Duration", "Total Fwd Packets", "Total Backward Packets", "Total Length of Fwd Packets", "Total Length of Bwd Packets", "Fwd Packet Length Max", "Fwd Packet Length Min", "Fwd Packet Length Mean", "Fwd Packet Length Std", "Bwd Packet Length Max", "Bwd Packet Length Min", "Bwd Packet Length Mean", "Bwd Packet Length Std", "Flow Bytes/s", "Flow Packets/s", "Flow IAT Mean", "Flow IAT Std", "Flow IAT Max", "Flow IAT Min", "Fwd IAT Total", "Fwd IAT Mean", "Fwd IAT Std", "Fwd IAT Max", "Fwd IAT Min", "Bwd IAT Total", "Bwd IAT Mean", "Bwd IAT Std", "Bwd IAT Max", "Bwd IAT Min", "Fwd PSH Flags", "Bwd PSH Flags", "Fwd URG Flags", "Bwd URG Flags", "Fwd Header Length", "Bwd Header Length", "Fwd Packets/s", "Bwd Packets/s", "Min Packet Length", "Max Packet Length", "Packet Length Mean", "Packet Length Std", "Packet Length Variance", "FIN Flag Count", "SYN Flag Count", "RST Flag Count", "PSH Flag Count", "ACK Flag Count", "URG Flag Count", "CWE Flag Count", "ECE Flag Count", "Down/Up Ratio", "Average Packet Size", "Avg Fwd Segment Size", "Avg Bwd Segment Size", "Fwd Header Length", "Fwd Avg Bytes/Bulk", "Fwd Avg Packets/Bulk", "Fwd Avg Bulk Rate", "Bwd Avg Bytes/Bulk", "Bwd Avg Packets/Bulk", "Bwd Avg Bulk Rate", "Subflow Fwd Packets", "Subflow Fwd Bytes", "Subflow Bwd Packets", "Subflow Bwd Bytes", "Init_Win_bytes_forward", "Init_Win_bytes_backward", "act_data_pkt_fwd", "min_seg_size_forward", "Active Mean", "Active Std", "Active Max", "Active Min", "Idle Mean", "Idle Std", "Idle Max", "Idle Min", "Label"


Technical information related to selected dataset subset (copied from the official dataset webpage)
---------------------------------------------------------------------------------------------------
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
   .. :widths: 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15 15

   +--------+---------+---------+---------+-----------+--------+----------+-------+-------+-------+-------+---------+--------+-----+------+-------+-------+-------+-------+-------+-------+--------+
   |        | Network | Traffic | Label.  | Interact. | Captu. | Protocols| ㅤ    | ㅤ     |  ㅤ   |  ㅤ   | Attack  |   ㅤ    |  ㅤ |  ㅤ  | ㅤ     | ㅤ    |  ㅤ   | Ano.  | Heter.| Feat. | Meta.  |
   |        |         |         |         |           |        | HTTP     | HTTPS | SSH   | FTP   | Email | Browser | Bforce | DoS | Scan | Bdoor | DNS   | Other |       |       |       |        |
   +========+=========+=========+=========+===========+========+==========+=======+=======+=======+=======+=========+========+=====+======+=======+=======+=======+=======+=======+=======+========+
   | DARPA  | ✅      | ❌      | ✅      | ✅        | ✅     | ✅       | ❌    | ✅    | ✅    | ❌    | ✅      | ✅     | ✅  | ❌   | ❌    | ✅    | ❌    | ❌    | ❌    | ✅    | ✅     |
   +--------+---------+---------+---------+-----------+--------+----------+-------+-------+-------+-------+---------+--------+-----+------+-------+-------+-------+-------+-------+-------+--------+
   | KDD’99 | ✅      | ❌      | ✅      | ✅        | ✅     | ✅       | ❌    | ✅    | ✅    | ❌    | ✅      | ✅     | ✅  | ❌   | ❌    | ✅    | ❌    | ❌    | ✅    | ✅    | ✅     |
   +--------+---------+---------+---------+-----------+--------+----------+-------+-------+-------+-------+---------+--------+-----+------+-------+-------+-------+-------+-------+-------+--------+
   | DEFCON | ❌      | ❌      | ❌      | ✅        | ✅     | ❌       | ✅    | ❌    | ❌    | ❌    | ❌      | ❌     | ✅  | ✅   | ❌    | ✅    | -     | ❌    | ❌    | ❌    | ❌     |
   +--------+---------+---------+---------+-----------+--------+----------+-------+-------+-------+-------+---------+--------+-----+------+-------+-------+-------+-------+-------+-------+--------+
   | CAIDA  | ✅      | ✅      | ❌      | ❌        | ❌     | -        | -     | -     | -     | ❌    | ❌      | ❌     | ✅  | ✅   | ❌    | ✅    | ✅    | ❌    | ❌    | ✅    | ❌     |
   +--------+---------+---------+---------+-----------+--------+----------+-------+-------+-------+-------+---------+--------+-----+------+-------+-------+-------+-------+-------+-------+--------+
   | LBNL   | ✅      | ✅      | ❌      | ❌        | ❌     | ✅       | ❌    | ✅    | ❌    | -     | -       | -      | ✅  | -    | -     | -     | ✅    | ❌    | ❌    | ❌    | ❌     |
   +--------+---------+---------+---------+-----------+--------+----------+-------+-------+-------+-------+---------+--------+-----+------+-------+-------+-------+-------+-------+-------+--------+
   | CDX    | ❌      | ❌      | ❌      | ✅        | ✅     | ❌       | ✅    | ✅    | ✅    | ❌    | ❌      | ✅     | ✅  | ❌   | ✅    | -     | -     | ❌    | ❌    | ❌    | ❌     |
   +--------+---------+---------+---------+-----------+--------+----------+-------+-------+-------+-------+---------+--------+-----+------+-------+-------+-------+-------+-------+-------+--------+
   | KYOTO  | ✅      | ❌      | ✅      | ✅        | ✅     | ✅       | ✅    | ✅    | ✅    | ✅    | ✅      | ✅     | ✅  | ✅   | ✅    | ✅    | ❌    | ❌    | ✅    | ✅    | ✅     |
   +--------+---------+---------+---------+-----------+--------+----------+-------+-------+-------+-------+---------+--------+-----+------+-------+-------+-------+-------+-------+-------+--------+
   | TWENTE | ✅      | ✅      | ✅      | ✅        | ✅     | ❌       | ✅    | ✅    | ❌    | ❌    | ✅      | ❌     | ✅  | ❌   | ❌    | ✅    | -     | -     | ❌    | ✅    | ❌     |
   +--------+---------+---------+---------+-----------+--------+----------+-------+-------+-------+-------+---------+--------+-----+------+-------+-------+-------+-------+-------+-------+--------+
   | UMASS  | ✅      | ❌      | ✅      | ❌        | ✅     | ❌       | ❌    | ❌    | ❌    | ❌    | ❌      | ❌     | ❌  | ❌   | ❌    | ✅    | -     | -     | ❌    | ❌    | ❌     |
   +--------+---------+---------+---------+-----------+--------+----------+-------+-------+-------+-------+---------+--------+-----+------+-------+-------+-------+-------+-------+-------+--------+
   | ISCX   | ✅      | ❌      | ✅      | ✅        | ✅     | ❌       | ✅    | ✅    | ✅    | ✅    | ✅      | ✅     | ✅  | ✅   | ✅    | ❌    | ✅    | ❌    | ✅    | ❌    | ✅     |
   +--------+---------+---------+---------+-----------+--------+----------+-------+-------+-------+-------+---------+--------+-----+------+-------+-------+-------+-------+-------+-------+--------+
   | ADFA   | ✅      | ✅      | ✅      | ✅        | ✅     | ❌       | ✅    | ✅    | ✅    | ✅    | ✅      | ❌     | ❌  | ✅   | ❌    | ✅    | ❌    | -     | ❌    | ✅    | ✅     |
   +--------+---------+---------+---------+-----------+--------+----------+-------+-------+-------+-------+---------+--------+-----+------+-------+-------+-------+-------+-------+-------+--------+
   | ISOT   | ✅      | ✅      | ✅      | ✅        | ✅     | ❌       | ❌    | ❌    | ✅    | ❌    | ❌      | ❌     | ❌  | ❌   | ❌    | ✅    | ✅    | ❌    | ❌    | ✅    | ❌     |
   +--------+---------+---------+---------+-----------+--------+----------+-------+-------+-------+-------+---------+--------+-----+------+-------+-------+-------+-------+-------+-------+--------+
   | SSHCure| ✅      | ✅      | ✅      | ✅        | ❌     | ❌       | ✅    | ❌    | ❌    | ❌    | ✅      | ❌     | ❌  | ❌   | ❌    | ❌    | ❌    | ❌    | ❌    | ✅    | ❌     |
   +--------+---------+---------+---------+-----------+--------+----------+-------+-------+-------+-------+---------+--------+-----+------+-------+-------+-------+-------+-------+-------+--------+
   | CTU-13 | ✅      | ✅      | ✅      | ✅        | ✅     | ❌       | ❌    | ❌    | ❌    | ✅    | ❌      | ✅     | ✅  | ✅   | ❌    | ✅    | ❌    | ❌    | ✅    | ✅    | ✅     |
   +--------+---------+---------+---------+-----------+--------+----------+-------+-------+-------+-------+---------+--------+-----+------+-------+-------+-------+-------+-------+-------+--------+
   | UGR'16 | ✅      | ✅      | ✅      | ✅        | ✅     | ✅       | ✅    | ✅    | ✅    | ❌    | ❌      | ✅     | ❌  | ✅   | ❌    | ✅    | ✅    | ❌    | ❌    | ✅    | ✅     |
   +--------+---------+---------+---------+-----------+--------+----------+-------+-------+-------+-------+---------+--------+-----+------+-------+-------+-------+-------+-------+-------+--------+
   | CICIDS | ✅      | ✅      | ✅      | ✅        | ✅     | ✅       | ✅    | ✅    | ✅    | ✅    | ✅      | ✅     | ✅  | ✅   | ✅    | ✅    | ✅    | ❌    | ✅    | ✅    | ✅     |
   +--------+---------+---------+---------+-----------+--------+----------+-------+-------+-------+-------+---------+--------+-----+------+-------+-------+-------+-------+-------+-------+--------+



Notes for Constantinos (to myself):
7 attack vector types
16 publicly available datasets and 11 distinct criteria based on what (ref)?
The extensive label set additionally demonstrates the authors' attempt to capture different types of attach without rersorting to simplistic binary classifications such as benign and nnon-benign.
pages 189-191 might contain useful info but it looks more CS heavy. Can someone look into them?

The original dataset contains with the full feature set evidently contains certain features that might not be as informative for classifying benign and malicious traffic. Naturally some variables will be more indicative of the nature behind a particular traffic flow. Following this rationale, the authors performed a statistical analysis that led to the conclusion that the following features had a higher impact: "flow
duration, inter-arrival time related features (for flow, forward and backward categories) and idle time related features." These results can be informative for Ethical Hacking researchers planning to collect data for traffic monitoring with a focus on detecting malicious traffic, as the authors point out that the aforementioned variables were indicative of malicious intent.
Stopped at p.194 (included).

 


sub header 1
-------------

This creates the toc on the right, in case we want to do it like that. however, that requires we use the same source page to add all content, which could get lengthly
