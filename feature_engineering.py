
def build_features(raw_data):
    return [
        raw_data["holder_concentration"],
        int(raw_data["mint_function"]),
        int(raw_data["lp_locked"]),
        raw_data["max_tax"],
        int(raw_data["owner_renounced"])
    ]
