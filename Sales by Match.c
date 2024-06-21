/* accepted in first attempt */

int sockMerchant(int n, int ar_count, int *ar)
{
    int socksCounter[101];
    int i, pairs = 0;

    for (i = 0; i < 101; i++)
        socksCounter[i] = 0;

    for (i = 0; i < n; i++)
    {
        socksCounter[ar[i]]++;

        if (socksCounter[ar[i]] != 0 && socksCounter[ar[i]] % 2 == 0)
            pairs++;
    }

    return pairs;
}