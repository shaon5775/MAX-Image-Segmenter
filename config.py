# Copyright 2018-2019 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# Flask settings
DEBUG = False

# Flask-restplus settings
RESTPLUS_MASK_SWAGGER = False
SWAGGER_UI_DOC_EXPANSION = 'none'

# Application settings

# API metadata
API_TITLE = 'MAX Image Segmenter'
API_DESC = 'Identify objects in an image, additionally assigning each pixel of the image to a particular object'
API_VERSION = '1.2.0'

# default model
MODEL_NAME = 'deeplab'
DEFAULT_MODEL_PATH = 'assets/{}'.format(MODEL_NAME)
MODEL_LICENSE = 'Apache v2'

MODEL_META_DATA = {
    'id': API_TITLE.lower().replace(' ', '-'),
    'name': API_TITLE,
    'description': 'DeepLab TensorFlow model for semantic image segmentation, trained on VOCO 2012',
    'type': 'Object Detection',
    'license': MODEL_LICENSE,
    'source': 'https://developer.ibm.com/exchanges/models/all/max-image-segmenter'
}

_FULL_MODEL_PATH = "assets/frozen_inference_graph_full.pb"
_MOBILE_MODEL_PATH = "assets/frozen_inference_graph_mobile.pb"
