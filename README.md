# Text Embeddings API

An embedding is a relatively low-dimensional space into which you can translate high-dimensional vectors. Embeddings make it easier to do machine learning on large inputs like sparse vectors representing words. Ideally, an embedding captures some of the semantics of the input by placing semantically similar inputs close together in the embedding space. An embedding can be learned and reused across models. 
[Embeddings Ref](https://developers.google.com/machine-learning/crash-course/embeddings/video-lecture)

Embeddings are commonly used for [OpenAI Ref](https://platform.openai.com/docs/guides/embeddings):
- Search
- Clustering (grouped by similarity)
- Recommendations
- Anomaly detection

[MediaPipe](https://developers.google.com/mediapipe) is a set of On-Device Machine Learning libraries ready for deployment in production. There are libraries for Android, iOS, Web, and Python. One of the multiple solutions is to create a numerical representation of text data, this means the embeddings.

This is an open-source code used MediaPipe for creating the embeddings and cosine as a similarity measure. This code is ready for deployment in GCP o another cloud platform. 

Once is deployed the request is like this:

```json
{
    "text1":"How's it going?",
    "text2":"I am fine"
}
```

The structure of the response is like this:

```json
{
    "text1embedding": "[127  16 185 127  82 127 128  50 127 127 172  10 127 128 127 127   7 160\n 128 128 128  90 127 238  70 127 246 128 127 127 170 128 182 185   9  76\n 154 196   4  42 136 127 127 127 128  28 151 127 127   4 135 127  80 157\n  77  90 113  41  15 127 128 167 127  83   1 127 217  60 128  90 255   2\n 161 232  24 171 127   9  55  12 127 210 127  87 181  79 127  88 128 124\n 128   7 128 128 128  19 127 127 250 145]",
    "text2embedding": "[127  44 209 127  35 127 128 128 127  81 176  26 127 128 127 127 242 180\n 139 128 128 127 127 147 126 127 230 128 127 127 200 137 128   9  65  70\n 217 128  22 124 142 127 118 127 194 131 128 127 110 245 142 127 127 151\n 127  50  67  61 248 127 128 128 127  36 216 127 218 106 151  78  20 223\n 182 189 222 233 127   1  76  11 127 253 127  33 186 127 127 235 128 121\n 128   4 128 128 175 187 127  87 228 141]",
    "similarity": 0.9128723626807329
}
```

Made with ❤ by  [jggomez](https://devhack.co).

[![Twitter Badge](https://img.shields.io/badge/-@jggomezt-1ca0f1?style=flat-square&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/jggomezt)](https://twitter.com/jggomezt)
[![Linkedin Badge](https://img.shields.io/badge/-jggomezt-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/jggomezt/)](https://www.linkedin.com/in/jggomezt/)
[![Medium Badge](https://img.shields.io/badge/-@jggomezt-03a57a?style=flat-square&labelColor=000000&logo=Medium&link=https://medium.com/@jggomezt)](https://medium.com/@jggomezt)

## License

    Copyright 2023 Juan Guillermo Gómez

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
