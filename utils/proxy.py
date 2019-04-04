import backend_ch1_sec1.settings

def proxy():
    if backend_ch1_sec1.settings.USE_PROXY:
        return {}
    else:
        return {}