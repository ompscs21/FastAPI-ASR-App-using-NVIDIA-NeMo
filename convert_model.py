from nemo.collections.asr.models import EncDecCTCModel

model = EncDecCTCModel.from_pretrained("stt_hi_conformer_ctc_medium")
model.export("onnx_model.onnx")

with open("vocab.txt", "w") as f:
    for token in model.decoder.vocabulary:
        f.write(f"{token}\n")
