
# 📰 Topic-RAG for Historical Newspapers

*Enhancing Information Retrieval in Humanities Research through Topic-Based Retrieval-Augmented Generation (RAG)*

---

## 📘 Overview

**Topic-RAG** is a framework designed to improve information retrieval and question answering over historical newspaper archives.  
It integrates **topic modeling** with **retrieval-augmented generation (RAG)** to enable focused, explainable, and efficient retrieval workflows for humanities research.

---

## 📂 Repository Structure

```
Topic-RAG-for-Historical-Newspapers/
│
├── translate/                  # Scripts for bulk translation to English
│   ├── translate_content.py
│   └── translate.sh
    └── translate_slurm.sh
│
├── topic_rag.py                # Core RAG pipeline for short documents and simple queries
├── topic_rag_plus.py           # Extended version with chunking for long documents
│
├── uid_list.txt                # List of unique Document IDs (UIDs)
├── keywords.txt                # Keywords used for dataset collection
│
├── README.md                   # This documentation file
     
```

---

## ⚙️ Translation

If your dataset contains non-English documents, please use the translation scripts in [`../translate/`](../translate/) for batch translation to English.

**Required installations:**
```bash
pip install googletrans==3.1.0a0 langdetect==1.0.9
```
> **Note:** Skip this step if your dataset is already in English.

---

## 🧹 Data Preparation

The data-cleaning process depends on the dataset type.  
Please follow the data-preparation steps described in our paper. After cleaning, create **document embeddings** (vector representations of text) for retrieval.

Once the data is prepared, you can use either of the following scripts:

- **`Topic-RAG`** – suitable for *short documents* and *simple queries*.  
- **`Topic-RAG+`** – includes a *chunking strategy* for efficiently handling *long documents* and *complex queries* that require retrieving many documents.

---

## 🔒 Data Access

Due to copyright restrictions, the dataset itself cannot be published.  
Access can be requested through the **Impresso platform**:

1. Register at [https://impresso-project.ch/app/](https://impresso-project.ch/app/)  
2. Accept the terms of use  
3. Sign the NDA: [https://impresso-project.ch/assets/documents/impresso_NDA.pdf](https://impresso-project.ch/assets/documents/impresso_NDA.pdf)  
4. Request access using the provided **UIDs** and **keywords**

> The authors do not manage Impresso user accounts or dataset distribution, so some delay in access may occur.

---

## 📄 UIDs & Keywords

- **UID list:** [`uid_list.txt`](./uid_list.txt)  
- **Keywords:** [`keywords.txt`](./keywords.txt)

These metadata files correspond to the Impresso dataset entries referenced in our experiments.

---

## 🙏 Acknowledgement

We thank the **Impresso team** for providing the document collection used in this study, developed as part of the project:  
> *“Impresso – Media Monitoring of the Past II. Beyond Borders: Connecting Historical Newspapers and Radio.”*

---

## 📚 Citation

If you use this repository or reference our approach, please cite:

```bibtex
@article{Topic-RAG-for-Historical-Newspapers2025,
  author  = {To be added},
  title   = {Topic-RAG for Historical Newspapers: Enhancing Information Retrieval in Humanities Research through Topic-Based Retrieval-Augmented Generation},
  journal = {To be added},
  year    = {2025}
}
```
-----
## License

This is an Open Access article, distributed under the terms of the Creative Commons Attribution-NonCommercial-NoDerivatives licence (http://creativecommons.org/licenses/by-nc-nd/4.0/), which permits non-commercial re-use, distribution, and reproduction in any medium, provided the original work is unaltered and is properly cited. The written permission of Cambridge University Press must be obtained for commercial re-use or in order to create a derivative work.
---

## 📩 Contact

For questions or clarifications, please contact the **corresponding author** listed in the original paper.
