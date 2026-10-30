#!/usr/bin/env python3
"""Password Audit Kit: local-only password strength education helper."""
import argparse, getpass, math, re, string

COMMON={"password","password123","123456","123456789","qwerty","qwerty123","admin","letmein","welcome","iloveyou"}
def assess(password):
    if not isinstance(password,str): raise TypeError("password must be a string")
    length=len(password); categories=sum(bool(set(chars)&set(password)) for chars in
        (string.ascii_lowercase,string.ascii_uppercase,string.digits,string.punctuation))
    findings=[]
    if length<12: findings.append("Use at least 12 characters; longer passphrases are often easier to remember.")
    if password.lower() in COMMON: findings.append("This password matches a very common weak password.")
    if re.search(r"(.)\1{3,}",password): findings.append("Avoid long repeated-character sequences.")
    if re.search(r"1234|abcd|qwerty|password",password,re.I): findings.append("Avoid predictable sequences and common words.")
    if categories<3: findings.append("Consider a longer passphrase or more variety; length matters more than complexity tricks.")
    # Deliberately conservative educational estimate, not a real crack-time prediction.
    pool=sum([26 if any(c.islower() for c in password) else 0,
              26 if any(c.isupper() for c in password) else 0,
              10 if any(c.isdigit() for c in password) else 0,
              32 if any(c in string.punctuation for c in password) else 0])
    entropy=round(length*math.log2(max(pool,1)),1) if password else 0
    if not findings: findings.append("No basic weaknesses detected. This does not prove the password is safe or unique.")
    return {"length":length,"character_categories":categories,"rough_entropy_bits":entropy,
            "findings":findings,"privacy":"Password is evaluated in memory only; this tool does not save or transmit it."}
def main():
    p=argparse.ArgumentParser(description="Local educational password check; input is not saved or transmitted.")
    p.add_argument("--stdin",action="store_true",help="Read password from stdin instead of hidden prompt")
    a=p.parse_args()
    password=input() if a.stdin else getpass.getpass("Password to assess (not displayed): ")
    print(__import__("json").dumps(assess(password),indent=2,ensure_ascii=False))
if __name__=="__main__": main()
