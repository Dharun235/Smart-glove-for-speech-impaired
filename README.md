# SHWASI smart glove

An Arduino-based assistive communication prototype using five flex sensors to recognize predefined finger-spelling gestures and send text/audio-oriented outputs through a connected application.

This repository contains the bachelor’s-thesis prototype, sensor-data collection code, exploratory machine-learning notebook, and Python-side inference utilities.

## Research context

- **Published phase:** [(SHWASI) Smart Hand Wearable Aid for Speech Impaired: Sign Language Communication using Flex Sensor-based Finger Spelling](https://ieeexplore.ieee.org/document/10958541), IEEE INDICON 2024, DOI [`10.1109/INDICON63790.2024.10958541`](https://doi.org/10.1109/INDICON63790.2024.10958541).
- **Thesis report:** [B.TechDissertationReport.pdf](https://github.com/Dharun235/dharun.github.io/blob/main/B.TechDissertationReport.pdf).
- **Follow-up work:** the data-collection and machine-learning extension is represented in this repository and is intended for a forthcoming publication. Treat those results as work in progress until that publication is available.

## How the prototype works

1. Five flex sensors are read through Arduino analog inputs `A0`–`A4`.
2. Sensor values are transmitted as comma-separated ADC readings.
3. A trained classifier maps five sensor values to an encoded gesture.
4. The main loop maps the gesture to a phrase, letter, number, or symbol.
5. The selected output can be forwarded through serial/Bluetooth to the companion application.

The gesture interface has three 32-entry modes:

- **Mode 1:** common phrases;
- **Mode 2:** alphabetic characters;
- **Mode 3:** numbers and special characters.

Start, stop, and mode-selection gestures are part of the control flow.

## Repository layout

```text
.
├── arduino_logger.ino             # Collect five-channel ADC samples
├── arduino_sender.ino             # Forward serial text over SoftwareSerial
├── read_from_arduino.py           # Read and classify serial sensor values
├── flex_to_num.py                 # Load a classifier and predict a gesture
├── Main loop.py                   # Map gesture IDs to user-facing outputs
├── ml_analysis_on_dataset.ipynb   # Dataset exploration and model experiments
├── lazy-predict.py                # Optional model-baseline comparison
├── Image of signs/                # Reference images for encoded gestures
├── requirements.txt               # Python dependencies
├── CODE_GUIDELINES.md             # Maintenance and attribution rules
├── CITATION.cff                   # Citation metadata
└── LICENSE                        # MIT code license and attribution notice
```

## Dataset

The associated [Fingerspelling Dataset](https://huggingface.co/datasets/Dharunkumar9/Fingerspelling_dataset) contains Excel recordings from five flex sensors. Its dataset card currently describes 96 files organized as 32 entries for each of the three modes, with `thumb`, `index`, `middle`, `ring`, and `little` sensor channels. The dataset is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); follow its attribution terms.

## Models

Trained model artifacts are kept outside this Git repository because of their size. The current model folder contains:

- `bagging_classifier.joblib`;
- `decision_tree.joblib`;
- `extra_trees_classifier.joblib`;
- `knn_classifier.joblib`;
- `random_forest.joblib`;
- `FFNN.h5`.

Models: [Google Drive model folder](https://drive.google.com/drive/u/4/folders/1gMEkVF_XD0_TCsYsYKikhC4BGvrp9c4A).

The repository currently performs inference in Python. The models are **not yet deployed to the Arduino**. Embedded deployment is a planned next step requiring a model compatible with the target board, conversion/quantization, memory and latency checks, and an on-device inference path.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

### Python inference

Set `SMART_GLOVE_MODEL` to a compatible classifier artifact, then use the serial reader or main loop:

```bash
export SMART_GLOVE_MODEL=/path/to/extra_trees_classifier.joblib
python read_from_arduino.py COM6
python "Main loop.py"
```

The existing scripts still require local serial-port configuration. Replace the example ports in `Main loop.py` with the ports exposed by the connected hardware.

### Arduino data collection

1. Open `arduino_logger.ino` in the Arduino IDE.
2. Select the connected board and serial port.
3. Upload the sketch.
4. Capture the comma-separated five-channel readings from the serial monitor or a serial logger.

`arduino_sender.ino` forwards text received over USB serial through `SoftwareSerial`; pin assignments and baud rate must match the hardware wiring.

## Reproducing the analysis

`ml_analysis_on_dataset.ipynb` is a Colab-oriented notebook. It explores the sensor data, class distribution, correlations, feature importance, clustering, PCA/t-SNE, neural-network training, classical classifiers, and serialized model artifacts. Update its Google Drive paths before running cells.

`lazy-predict.py` is an optional baseline script. It expects an Excel file with five sensor columns followed by a `label` column and uses `LazyClassifier` to compare candidate classifiers.

## Citation

For academic or public use, cite the published paper, thesis report, dataset, and this repository. Do not present the prototype or unpublished extension as independent work.

```bibtex
@inproceedings{10958541,
  author    = {E, Mithun and S, Dharun Kumar and A, Abirami and J, Mathiarasun R and E, Harikumar M},
  title     = {(SHWASI) Smart Hand Wearable Aid for Speech Impaired: Sign Language Communication using Flex Sensor-based Finger Spelling},
  booktitle = {2024 IEEE 21st India Council International Conference (INDICON)},
  year      = {2024},
  pages     = {1--6},
  doi       = {10.1109/INDICON63790.2024.10958541}
}
```

## License

Source code is released under the [MIT License](LICENSE). The dataset has separate [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) terms. This repository is a reference release; it has no external contribution workflow.
