with open("/scone/iexec_out/my-result.txt", "w+") as fout:
    message = "Hello from inside the enclave, it's dark over here!"

    # print to stdout
    print(message)

    # write result file in /scone/iexec_out
    fout.write(message)
