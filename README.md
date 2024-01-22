# Measuring Consistency in Text-based Financial Forecasting Models

## Citation
If you find this repository helps your research, please cite our following paper:
```bibtex
@article{yang2023measuring,
  title={Measuring Consistency in Text-based Financial Forecasting Models},
  author={Yang, Linyi and Ma, Yingpeng and Zhang, Yue},
  journal={arXiv preprint arXiv:2305.08524},
  year={2023}
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


