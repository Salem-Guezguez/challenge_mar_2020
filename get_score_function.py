
def get_score(r1, r2):
    # both are Developer
    if len(r1) == 3 and len(r2) == 3:
        # calculate work potential
        skills1 = r1[2]
        skills2 = r2[2]
        nb_common_skills = len(skills1.intersection(skills2))
        nb_different_skills = len(skills1.union(skills2)) - nb_common_skills
        wp = nb_common_skills * nb_different_skills
    else:
        wp = 0
    bp = 0
    if r1[0] == r2[0]:
        bp = r1[1]*r2[1]
    return bp + wp


if __name__ == "__main__":
    d0 = ('opn', 7, {'java', 'bpm'})
    d1 = ('clstr', 5, {'python', 'azure'})
    d2 = ('mac', 1, {'nlp', 'big_data'})
    d3 = ('clstr', 3,  {'azure', 'c#'})
    m0 = ('opn', 2)
    m1 = ('mac', 5)
    print(get_score(d2, d3))