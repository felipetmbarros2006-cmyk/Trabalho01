def autenticar(usuario, senha, usuarios):
    if usuario in usuarios:
        if usuarios[usuario] == senha:
            return True
    return False
