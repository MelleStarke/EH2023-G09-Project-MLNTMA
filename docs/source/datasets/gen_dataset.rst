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
      
      * Description of how it was made/collected \(e.g. NMAP\)
      * Related work
      * How it relates to Ethical Hacking \(more line a general requirement of this section\)
      * Description of PCAP and relation to extracted features in the csv \(lower priority than the rest\)

   Feel free to add to this.

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
 


sub header 1
-------------

This creates the toc on the right, in case we want to do it like that. however, that requires we use the same source page to add all content, which could get lengthly
