# 🔍 FactFlow

> An Agentic AI system for real-time misinformation detection and evidence retrieval

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Status](https://img.shields.io/badge/status-in%20development-orange.svg)]()

## 🎯 Overview

FactFlow is an intelligent AI agent that goes beyond traditional fake news detection. It not only predicts whether content is misinformation, but also **explains its reasoning** and **retrieves contradictory evidence** from trusted sources in real-time.

Unlike basic classifiers, FactFlow combines explainable ML with agentic reasoning to provide transparent, verifiable fact-checking.

## ✨ Key Features

- **🤖 ML-Powered Detection**: Advanced classification using TF-IDF/BERT for accurate fake news prediction
- **🔍 Evidence Retrieval**: Autonomous web search agent that finds contradictory sources from trusted domains
- **💡 Explainable AI**: SHAP/LIME visualizations showing exactly why content was flagged
- **🧠 LLM Summarization**: Natural language explanations of contradictions using GPT/Gemini
- **⚡ Real-Time Analysis**: Instant processing and verification of news articles and social media posts

## 🚀 How It Works

```
User Input (Article/Tweet)
        ↓
[ML Classifier] → Probability Score (Fake/Real)
        ↓
[Explainability] → SHAP visualization of key suspicious tokens
        ↓
[Search Agent] → Retrieves fact-checks from Reuters, BBC, etc.
        ↓
[LLM Summarizer] → Generates human-readable contradiction summary
        ↓
Final Report: Score + Evidence + Explanation
```

## 🛠️ Tech Stack

| Layer | Technologies |
|-------|-------------|
| **Core ML** | scikit-learn, XGBoost, TF-IDF, BERT |
| **Explainability** | SHAP, LIME |
| **Retrieval** | DuckDuckGo Search API, SerpAPI |
| **LLM Integration** | GPT-4o, Gemini, Hugging Face |
| **Frontend** | Streamlit |
| **Backend** | FastAPI (optional) |

## 📁 Project Structure

```
FactFlow/
│
├── data/
│   └── train.csv                    # Training dataset
│
├── src/
│   ├── preprocessing.py             # Text cleaning and feature extraction
│   ├── model_training.py            # ML model training pipeline
│   ├── explainability.py            # SHAP/LIME integration
│   ├── web_agent.py                 # Evidence retrieval agent
│   └── summarizer.py                # LLM-based contradiction summary
│
├── app/
│   └── app.py                       # Streamlit frontend
│
├── models/
│   ├── fake_news_model.pkl          # Trained classifier
│   └── vectorizer.pkl               # TF-IDF vectorizer
│
├── requirements.txt
└── README.md
```

## 🔧 Installation

> **Note**: Project is in early development. Installation instructions will be updated as modules are completed.

```bash
# Clone the repository
git clone https://github.com/yourusername/factflow.git
cd factflow

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (coming soon)
pip install -r requirements.txt
```

## 📊 Example Usage

```python
# Example workflow (API under development)
from factflow import FactFlowAnalyzer

analyzer = FactFlowAnalyzer()

article = "NASA confirms aliens exist, says leaked internal document."

result = analyzer.analyze(article)

print(f"Prediction: {result.label} ({result.probability}%)")
print(f"Evidence: {result.sources}")
print(f"Explanation: {result.summary}")
```

**Expected Output:**
```
Prediction: 🚨 Likely Fake (94% probability)

Key Suspicious Tokens: "aliens", "leaked", "internal document"

Evidence Sources:
• NASA Official Press Release - No evidence found
• Reuters Fact Check - Debunked claim

Summary: Trusted sources including NASA and Reuters deny any such 
discovery. This claim contradicts verified information from official channels.
```

## 🎯 Roadmap

- [x] Project structure setup
- [ ] Data preprocessing pipeline
- [ ] ML model training (TF-IDF + Logistic Regression)
- [ ] SHAP explainability integration
- [ ] Web search agent implementation
- [ ] LLM summarization module
- [ ] Streamlit UI development
- [ ] End-to-end testing
- [ ] Documentation and demo video

## 🤝 Contributing

This project is currently in active development for HackInfinity 2025. Contributions, suggestions, and feedback are welcome!

## 📄 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

### What this means:
- ✅ You can use, modify, and distribute this software
- ✅ You can use it for commercial purposes
- ⚠️ Any derivative work must also be open-source under GPL-3.0
- ⚠️ You must disclose the source code when distributing
- ⚠️ You must include the original license and copyright notice

## 👨‍💻 Author

Built with ⚡ by [Vansh-09]

---

**Status**: 🚧 Active Development | **Target**: Production-ready for HackInfinity 2025
