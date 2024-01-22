# Measuring Consistency in Text-based Financial Forecasting Models

## Citation
If you find this repository helps your research, please cite our following paper:
```bibtex
@inproceedings{yang-etal-2023-measuring,
    title = "Measuring Consistency in Text-based Financial Forecasting Models",
    author = "Yang, Linyi and Ma, Yingpeng and Zhang, Yue",
    booktitle = "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    year = "2023",
    publisher = "Association for Computational Linguistics",
    pages = "13751--13765"
 }
```

## Intro
The repository for ACL-2023 paper [Measuring Consistency in Text-based Financial Forecasting Models](https://aclanthology.org/2023.acl-long.769/).
We provide our code used for the paper. 

## Dataset
The raw dataset of the earnings call can be found from [Qin and Yang, ACL-19](https://github.com/GeminiLn/EarningsCall_Dataset).
Previous works all have divided the earnings call dataset into mutually exclusive train/validation/test sets in a 7:1:2 ratio based on chronological order. 
In line with this approach, we obtained the testset and expanded the testset by generating four consistency test sets to evaluate the consistency for model.

## Code
Also, we have provided the code we used to generate consistency test examples, to enable researchers to extend their own datasets into a form suitable for testing consistency.

## Contact
If you have any questions or concerns, please feel free to email me at mayingpeng33 AT gmail DOT com  -- Thanks for reading.


