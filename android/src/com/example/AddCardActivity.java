package com.example;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;


public class AddCardActivity extends Activity {

    private EditText etFirstName;
    private EditText etLastName;

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.add_card);
        Button addButton=(Button)findViewById(R.id.okButton);
         etFirstName=(EditText)findViewById(R.id.FirstName);
         etLastName=(EditText)findViewById(R.id.LastName);

        View.OnClickListener onClickListener = new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                switch (view.getId()){
                    case R.id.okButton:
                        Intent intent=new Intent();
                        String firstName= etFirstName.getText().toString();
                        String lastName=etLastName.getText().toString();
                        intent.putExtra("FirstName",firstName);
                        intent.putExtra("LastName", lastName);
                        setResult(RESULT_OK, intent);
                        AddCardActivity.this.finish();
                        break;
                }
            }
        };
        addButton.setOnClickListener(onClickListener);
    }


}
