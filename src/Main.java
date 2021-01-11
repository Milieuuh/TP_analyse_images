import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class Main extends Application {

        @Override
        public void start(Stage primaryStage) throws Exception{
            Group root = new Group() ;
            primaryStage.setScene(new Scene(root, 1200, 950));
            fenetre f = new fenetre(primaryStage);
            root.getChildren().add(f) ;
            primaryStage.show();
        }


        public static void main(String[] args) {
            launch(args);
        }
}


