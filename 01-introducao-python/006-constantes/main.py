def constantes():
    VELOCIDADE_DA_LUZ = 299792458
    print(f"Velocidade da luz é: {VELOCIDADE_DA_LUZ} m/s")

    try:
        VELOCIDADE_DA_LUZ = 300000000
    except Exception as e:
        print(f"Erro ao tentar alterar a constante: {e}")

if __name__ == '__main__':
    constantes()