<div align="center">

# Sportfolio

### Computer-vision-based sports movement analysis

**Python · Research-oriented AI · Reproducible experiments**

`IN PROGRESS` · Initial public project scaffold

</div>

---

## Overview

A focused computer-vision prototype investigating whether pretrained pose estimation can support interpretable measurements for a selected movement under controlled recording conditions.

This repository is being developed as part of a portfolio exploring **reliable, explainable, and evidence-aware AI systems**. The current README describes the intended scope and methodology. Features are marked complete only after they have been implemented and tested.

## Problem statement

Pose-estimation models make body landmarks accessible from ordinary video, but 2D landmarks are affected by camera placement, occlusion, lighting, and viewpoint. A responsible prototype should communicate these constraints rather than make unsupported claims about athletic ability or injury risk.

## Research question

> How reliably can a single-camera pose-estimation pipeline extract interpretable movement measurements for a selected exercise, and how do camera angle, lighting, and landmark visibility affect those measurements?

## Objectives

- [ ] Video upload and frame sampling
- [ ] Pretrained pose estimation using MediaPipe
- [ ] Initial scope limited to one movement, such as a bodyweight squat
- [ ] 2D joint-angle calculations from visible landmarks
- [ ] Landmark overlays and measurement traces over time
- [ ] Rule-based educational feedback with visibility/confidence indicators
- [ ] Controlled recordings and manually checked reference frames

## Proposed methodology

The project will be developed through explicit baselines, documented implementation choices, and evaluation on a defined dataset or test collection. The exact experimental configuration and results will be added after implementation and validation.

## System architecture

The following diagram represents the **planned** system flow, not a claim that every component is already implemented.

```mermaid
flowchart TD\n A[Uploaded video] --> B[Frame extraction]\n B --> C[Pose landmark model]\n C --> D[Landmark visibility and confidence checks]\n D --> E[2D joint-angle calculations]\n E --> F[Movement timeline and visual overlay]\n F --> G[Rule-based educational feedback]\n G --> H[Evaluation and limitations report]
```

## Evaluation strategy

- Define a consistent camera setup and movement protocol
- Measure landmark detection availability and confidence
- Compare selected joint-angle estimates with manually annotated reference frames
- Test repeatability across recordings
- Document changes under different lighting, clothing, and camera positions

Evaluation results will be reported with dataset provenance, split strategy, relevant metrics, and representative failure cases. No performance figures are claimed in this initial scaffold.

## Technology stack

Python, Streamlit, OpenCV, MediaPipe, NumPy, pandas, matplotlib

## Repository structure

```text
sportfolio/
├── app.py                  # Streamlit entry point
├── src/
│   └── sportfolio/
│       └── __init__.py
├── data/                   # Local datasets; large/private data excluded from Git
├── reports/                # Experiment protocols and evaluation reports
├── assets/
│   └── screenshots/        # Add genuine application screenshots here
├── tests/                  # Automated tests
├── requirements.txt
├── .env.example
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Getting started

### Prerequisites

- Python 3.10 or newer (verify package-specific compatibility during setup)
- Git
- A virtual environment

### Clone

```bash
git clone https://github.com/itirksnasingh/sportfolio.git
cd sportfolio
```

### Create a virtual environment

**Windows PowerShell**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
python -m venv .venv
source .venv/bin/activate
```

### Install dependencies and run

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

The current app is an informational scaffold. Core project workflows will be added as development progresses.

## Development roadmap

- [ ] Repository scaffold and project documentation
- [ ] Video upload and frame processing
- [ ] Pose landmark detection and visualization
- [ ] Single-movement segmentation / analysis
- [ ] Joint-angle calculations
- [ ] Feedback rules and confidence display
- [ ] Controlled evaluation and error analysis
- [ ] Deployment and demo documentation

## Limitations and responsible use

- A single camera provides 2D image measurements, not reliable full 3D biomechanics.
- Results are sensitive to viewpoint, occlusion, clothing, lighting, and frame quality.
- The prototype is educational and is not a medical, injury-risk, or talent-diagnosis tool.
- Claims about accuracy require an explicitly annotated reference set.

## Current status

| Area | Status |
|---|---|
| Project scope and research question | Defined |
| Repository scaffold and documentation | Prepared |
| Core implementation | In progress |
| Evaluation and results | Pending |
| Deployment | Pending |

## Reproducibility and data policy

- Record dataset name, source, version, and license.
- Do not commit private, sensitive, or unlicensed data.
- Keep credentials in local environment variables or hosting secrets.
- Record model versions, random seeds, preprocessing, and evaluation configuration.
- Distinguish measured results from hypotheses and planned work.

## Author

**Sanskriti Singh**  
B.Tech Computer Science (AI/ML)  
Bharati Vidyapeeth (Deemed to be University)

## License

This project is released under the MIT License. Dataset, pretrained-model, and third-party component licenses remain subject to their respective terms.
