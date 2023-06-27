use std::env;
use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

fn main() -> std::io::Result<()>{
    let args: Vec<String> = env::args().collect();
    assert_eq!(args.len(), 3);
    let mut file = File::create("foo.txt")?;
    file.write(args[1].as_bytes())?;
    file.write(b"\n")?;
    file.write(args[2].as_bytes())?;
    file.write(b"\n")?;
    let x: [u8; 13] = [32, 33, 34, 35, 44, 55, 66, 99, 123, 124, 125, 126, 127];
    file.write(&x)?;
    //let mut buf_reader = BufReader::new(file);
    let mut file1 = File::open("foo.txt")?;
    let mut contents = String::new();
    file1.read_to_string(&mut contents)?;
    print!("{}",contents);
    
    Ok(())
}
