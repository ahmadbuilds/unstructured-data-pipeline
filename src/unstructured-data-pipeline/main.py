from application.pipelines.llm_pipeline import create_agent_instance,format_template
from infrastructure.CLI.main import read_files
from domain.schema.invoice import Invoice,ItemDetails
from config import COMMAND

react_agent=create_agent_instance()
invoice_schema=Invoice()
ItemDetails_schema=ItemDetails()

print("=====Welcome to Unstructured Data Pipeline======")
print("for help type Commands")

while(True):
    command=input()
    if command.strip()=="Commands":
        print("Exit")
        print(COMMAND)
    elif command.strip()=="Exit":
        break
    else:
        chunks=command.strip().split(" ")
        
        if len(chunks) < 4:
            print("Invalid command format. Expected: process <input_path> --db <output_db_path>")
            continue
        
        if chunks[0].lower() != "process":
            print("Invalid command. First argument must be 'process'")
            continue
        
        if "--db" not in chunks:
            print("Invalid command format. Missing '--db' flag")
            continue
        
        try:
            input_path = chunks[1]
            
            # Find --db flag and get output database path
            db_index = chunks.index("--db")
            if db_index + 1 >= len(chunks):
                output_db_path=None
            else:
                output_db_path = chunks[db_index + 1]
            
            # Read and validate files
            file_contents = read_files([input_path] if type(input_path) == str else input_path)
            
            if file_contents:
                print(f"Successfully processed {len(file_contents)} file(s)")
                
                for content in file_contents:
                    print("\nProcessing file content...")
                    
                    formatted_template=format_template(
                        invoice_schema,ItemDetails_schema,content,output_db_path
                    )
                    response = react_agent.invoke(
                        {"input":formatted_template}
                    )
                    
                    print("Processing complete.")
            else:
                print("No valid files to process.")
        except Exception as e:
            print(f"Error processing files: {str(e)}")
