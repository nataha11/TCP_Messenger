import socket
import sys
import select

def main():
    #Create a TCP socket
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    #Read ip from stdin, establish connection to the server
    ipaddr = str(sys.stdin.readline()).strip(' \n')
    conn.connect((ipaddr, 7855))
    conn_fobj = conn.makefile('rw', encoding='utf-8')
    #Create poll object for stdin and socket
    stdin_fd = sys.stdin.fileno()
    poll_array = select.poll()
    poll_array.register(stdin_fd, select.POLLIN)
    poll_array.register(conn, select.POLLIN)
    #Handle input and incoming data:
    running = True
    try:
        while running:
            for fd, event in poll_array.poll():
                if fd == stdin_fd:
                    line = sys.stdin.readline()
                    conn_fobj.write(line)
                    conn_fobj.flush()
                else:
                    if event == select.POLLIN:
                        line = conn_fobj.readline()
                        if len(line) > 0:
                            sys.stdout.write(line)
                            continue

                        print('Disconnected')
                        running = False
                        break
    except KeyboardInterrupt:
        conn.shutdown(socket.SHUT_RDWR)
    #Close connection:
    conn.close()


if __name__ == '__main__':
    main()
