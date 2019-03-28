import random

import turingarena as ta

for _ in range(10):
    z = random.randint(-500, 500)

    try:
        with ta.run_algorithm(ta.submission.source) as process:
            n = process.functions.rank(z)
            zz = process.functions.unrank(n)
    except ta.AlgorithmError as e:
        ta.goals["correct"] = False
        print(e)
    if z == zz:
       print(f"Correct! Hai codificato in numero intero {z} nel numero naturale {n} e la tua decodifica ti ha correttamente decodificato {n} come {zz}")
    else:
       ta.goals.setdefault("correct", False)
       print(f"Pias menga! Hai codificato in numero intero {z} nel numero naturale {n} ma poi, mi decodifichi {n} come {zz}, invece che tornarmi in {z}.")
        
ta.goals.setdefault("correct", True)
print(ta.goals)

