def eligible_to_vote(age):
   
    if age >= 18:
        print("You possess the right to cast a ballot.")
    else:
        print("Voting is not available to you.")


us_age = int(input("Input Your Age: "))

eligible_to_vote(us_age)
