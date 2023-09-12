use std::fs::File;
use std::io::Read;

fn main() {
    // Open the file
    let mut file = match File::open("path/to/your/file.txt") {
        Ok(file) => file,
        Err(error) => panic!("Failed to open file: {}", error),
    };

    // Read the contents of the file into a string
    let mut contents = String::new();
    match file.read_to_string(&mut contents) {
        Ok(_) => {
            println!("File contents:\n{}", contents);
        }
        Err(error) => {
            panic!("Failed to read file: {}", error);
        }
    }
}