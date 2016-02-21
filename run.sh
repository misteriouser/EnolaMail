echo "Number of mails to send: "
read number
times=$(((number / 50)))
time=$((0))
while [ "$time" -lt "$times" ]; do
    python3 enolamail.py    
    secs=$((120))    
    time=$((time + 1))
    echo "Sent -> $((time * 50))"
    if [ "$time" -ne "$times" ];
    then
        while [ $secs -gt 0 ]; do
            echo -ne "$secs\033[0K\r"
            sleep 1
            : $((secs--))
        done
    fi
done

