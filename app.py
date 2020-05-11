with open("/scone/iexec_out/my-result.txt", "w+") as result_file:
    message = "Hello from inside the enclave, it's dark over here!"

    # print to stdout
    print(message)

    # write result file in /scone/iexec_out
    result_file.write(message)
