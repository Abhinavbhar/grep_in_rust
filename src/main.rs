use std::{env, error, fs::File, io::Read};
fn main() {
    let args:Vec<String>=env::args().collect();
    let file_path :String = args[1].clone();
    let word :String = args[2].clone();

    println!("filepath:{},word:{}",file_path,word);
    let mut file =match File::open(file_path){
        Ok(file) => file,
        Err(error)=>{
            println!("Failed to open the file {}",error);
            return;
        }
    };
    
    let mut contents =String::new();
    file.read_to_string(&mut contents).unwrap();
    let ans:bool=contents.contains(&word);
    match ans {
        true=>println!("found the word"),
        false=>println!("did not find the word")
    }
    println!("contents of the file is {}",contents);

}
