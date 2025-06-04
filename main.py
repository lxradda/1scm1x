
from utils.onchain_checker import get_contract_features
from utils.feature_engineering import build_features
from utils.code_analysis import analyze_contract_code
import joblib

model = joblib.load("models/scam_model.pkl")

def analyze(contract_address):
    features = get_contract_features(contract_address)
    flags = analyze_contract_code(contract_address)
    X = build_features(features)
    risk = model.predict_proba([X])[0][1] * 100

    return {
        "contract": contract_address,
        "risk_score": round(risk, 2),
        "red_flags": flags
    }
