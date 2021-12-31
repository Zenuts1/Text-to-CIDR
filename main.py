import re
def main():
    input = open('input', 'r')
    output = open('output', 'a')
    re_ip = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,3}")
    for line in input:
        ip = re.findall(re_ip,line)
        output.write("{}\n".format(ip))
    input.close()
    output.close()
main()