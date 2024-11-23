
def convert_to_binary(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "wb") as outfile:
            for line in infile:
                # Ignorar comentários e linhas em branco
                line = line.strip()
                if not line or ";" in line:
                    line = line.split(";")[0].strip()  # Remover comentário após o ";"
                    if not line:
                        continue  # Ignorar linha se estiver vazia após remover o comentário
                
                # Separar os valores hexadecimais
                hex_values = line.split()
                byte_array = []

                for value in hex_values:
                    try:
                        # Convertendo os valores hexadecimais em bytes
                        byte_array.append(int(value, 16))
                    except ValueError:
                        print(f"Ignoring invalid hex value: {value}")

                # Preencher com zeros se houver menos de 16 bytes
                if len(byte_array) < 16:
                    byte_array += [0] * (16 - len(byte_array))

                # Escrever os 16 bytes no arquivo binário
                outfile.write(bytearray(byte_array))

        print(f"File successfully converted to binary: {output_file}")

    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except IOError as e:
        print(f"Error reading or writing files: {e}")


def main():
    input_file = input("Enter the input file name (.txt): ").strip()
    if not input_file.endswith(".txt"):
        print("Invalid input file format. Please provide a '.txt' file.")
        return

    output_file = input_file.replace(".txt", ".dat")
    convert_to_binary(input_file, output_file)


if __name__ == "__main__":
    main()
