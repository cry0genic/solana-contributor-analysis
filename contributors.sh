#!/bin/sh

a=1
while [ $a -le 13 ]

do
    echo "$(curl \
        -H "Accept: application/vnd.github.v3+json" \
        https://api.github.com/repos/solana-labs/solana/contributors?page=$a)" >> response.json
    a=$((a+1))
done
