#include <bits/stdc++.h>
using namespace std;

string plainAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
string cipherAlphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"; // custom key

string encrypt(string text)
{
    string result = "";

    for (char ch : text)
    {
        if (isalpha(ch))
        {
            bool isUpper = isupper(ch);
            char upperChar = toupper(ch);

            int index = plainAlphabet.find(upperChar);
            char encryptedChar = cipherAlphabet[index];

            if (!isUpper)
                encryptedChar = tolower(encryptedChar);

            result += encryptedChar;
        }
        else
        {
            result += ch; // non-letter unchanged
        }
    }

    return result;
}

string decrypt(string cipherText)
{
    string result = "";

    for (char ch : cipherText)
    {
        if (isalpha(ch))
        {
            bool isUpper = isupper(ch);
            char upperChar = toupper(ch);

            int index = cipherAlphabet.find(upperChar);
            char decryptedChar = plainAlphabet[index];

            if (!isUpper)
                decryptedChar = tolower(decryptedChar);

            result += decryptedChar;
        }
        else
        {
            result += ch;
        }
    }

    return result;
}

int main()
{
    string text;
    cout << "Enter text: ";
    getline(cin, text);

    string encrypted = encrypt(text);
    string decrypted = decrypt(encrypted);

    cout << "Original: " << text << endl;
    cout << "Encrypted: " << encrypted << endl;
    cout << "Decrypted: " << decrypted << endl;

    return 0;
}