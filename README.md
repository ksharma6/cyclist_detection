In the following repository, I created a cyclist detection model that is able to identify cyclists in incoming image data

Dataset url: https://www.kaggle.com/datasets/semiemptyglass/cyclist-dataset/data

Context

I'm not owner the of this dataset, all the credit goes to X. Li, F. Flohr, Y. Yang, H. Xiong, M. Braun, S. Pan, K. Li and D. M. Gavrila, the creators of this dataset.
Content

- img size - 2048x1024
- 13.7k labeled images (1000 images have no cyclists)
- labels in yolo format: id center_x center_y width height (relative to image width and height)

Example yolo bounding box:

`0 0.41015625 0.44140625 0.0341796875 0.11328125`

Acknowledgments
License Terms

This dataset is made freely available non-commercial purposes such as academic research, teaching, scientific publications, or personal experimentation. Permission is granted to use, copy, and distribute the data given that you agree:

- That the dataset comes "AS IS", without express or implied warranty. Although every effort has been made to ensure accuracy, Daimler (or the website host) does not accept any responsibility for errors or omissions.
- That you include a reference to the above publication in any published work that makes use of the dataset.
- That if you have altered the content of the dataset or created derivative work, prominent notices are made so that any recipients know that they are not receiving the original data.
- That you may not use or distribute the dataset or any derivative work for commercial purposes as, for example, licensing or selling the data, or using the data with a purpose to procure a commercial gain.
- That this original license notice is retained with all copies or derivatives of the dataset.
- That all rights not expressly granted to you are reserved by Daimler.

Citation
`X. Li, F. Flohr, Y. Yang, H. Xiong, M. Braun, S. Pan, K. Li and D. M. Gavrila. A New Benchmark for Vision-Based Cyclist Detection. In Proc. of the IEEE Intelligent Vehicles Symposium (IV), Gothenburg, Sweden, pp.1028-1033, 2016`