import onnxruntime
import numpy as np

class ASRModel:
    def __init__(self, model_path: str, vocab_path: str):
        self.session = onnxruntime.InferenceSession(model_path, providers=["CPUExecutionProvider"])
        self.vocab = self._load_vocab(vocab_path)

    def _load_vocab(self, vocab_path):
        with open(vocab_path, 'r', encoding='utf-8') as f:
            labels = f.read().splitlines()
        return labels

    def decode(self, logits):
        best_path = np.argmax(logits, axis=-1)
        decoded = []
        prev = -1
        for i in best_path:
            if i != prev and i != 0:
                decoded.append(self.vocab[i])
            prev = i
        return ''.join(decoded)

    def transcribe(self, input_features: np.ndarray) -> str:
        ort_inputs = {"audio_signal": input_features}
        ort_outs = self.session.run(None, ort_inputs)
        return self.decode(ort_outs[0])
