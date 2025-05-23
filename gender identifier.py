g = input("Enter the gender: ").strip().lower()

male_terms = {'male', 'm'}
female_terms = {'female', 'f'}
nonbinary_terms = {'non-binary', 'nonbinary', 'nb', 'other', 'prefer not to say', 'unknown'}

if g in male_terms:
    print("Male")
elif g in female_terms:
    print("Female")
elif g in nonbinary_terms:
    print("Non-binary / Other")
else:
    print("Gender not recognized")
