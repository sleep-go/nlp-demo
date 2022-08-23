import paddlenlp

MODEL_NAME = "ernie-3.0-medium-zh"
ernie_model = paddlenlp.transformers.ErnieModel.from_pretrained(MODEL_NAME)